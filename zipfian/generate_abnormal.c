#include <stdio.h>
#include <stdlib.h>

#define DATA_SIZE 5000000
#define MAX_DATA_VALUE 2800000
#define NUM_BINS 30  // You can adjust the number of bins as needed

int main() {

    // Assuming each line in the file contains one integer
    int item;

    int index = 0;


    int *data;  // Assuming your data is stored in an array
    data = (int *)malloc(DATA_SIZE * sizeof(int));


    // Open the file for reading
    FILE *file = fopen("normal_requests_5m.csv", "r");


    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }


    while (fscanf(file, "%d", &item) == 1) {
        data[index]= item;
        index++;
    }

    // Close the file
  fclose(file);
  printf("file read already\n");
  fflush(stdout);

    // Initialize your data array with your actual data here
    // For example, you can generate random data or read from a file


    file = fopen("abnormal_requests_5m.csv", "w");


    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }


    // Print the histogram
    for (int i = 0; i < DATA_SIZE; i++) {
        fprintf(file, "%d\n", 2800000 - data[i]);
    }

    fclose(file);

    return 0;
}
