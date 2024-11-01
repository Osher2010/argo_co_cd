#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <microhttpd.h>

#define PORT 8888
#define UPLOAD_DIR "uploads/"

struct upload_status {
    FILE *fp;
    size_t remaining;
};

int answer_to_connection(void *cls, struct MHD_Connection *connection,
                         const char *url, const char *method,
                         const char *version, const char *upload_data,
                         size_t *upload_data_size, void **con_cls) {
    if (strcmp(method, "POST") != 0) {
        return MHD_NO; // Only accept POST requests
    }

    struct upload_status *status = *con_cls;

    if (status == NULL) {
        status = malloc(sizeof(struct upload_status));
        if (status == NULL) {
            return MHD_NO;
        }
        status->fp = NULL;
        status->remaining = 0;

        *con_cls = status;
        return MHD_YES;
    }

    if (status->fp == NULL) {
        char *filename = "uploads/uploaded_file"; // Set the filename
        status->fp = fopen(filename, "wb");
        if (status->fp == NULL) {
            free(status);
            return MHD_NO;
        }
        status->remaining = 1024 * 1024 * 10; // Limit file size to 10MB
    }

    if (*upload_data_size > 0) {
        size_t to_write = *upload_data_size < status->remaining ? *upload_data_size : status->remaining;
        fwrite(upload_data, 1, to_write, status->fp);
        status->remaining -= to_write;
        *upload_data_size -= to_write;
        return MHD_YES;
    }

    fclose(status->fp);
    free(status);
    *con_cls = NULL;
    return MHD_HTTP_OK;
}

int main() {
    struct MHD_Daemon *daemon;

    // Create the upload directory if it doesn't exist
    mkdir(UPLOAD_DIR, 0777);

    daemon = MHD_start_daemon(MHD_USE_SELECT_INTERNALLY, PORT, NULL, NULL,
                               &answer_to_connection, NULL, MHD_OPTION_END);
    if (daemon == NULL) {
        return 1;
    }

    printf("Server is running on port %d\n", PORT);
    getchar(); // Wait for user input to exit

    MHD_stop_daemon(daemon);
    return 0;
}
