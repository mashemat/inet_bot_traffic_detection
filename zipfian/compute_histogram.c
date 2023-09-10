#include <stdio.h>
#include <stdlib.h>

#define DATA_SIZE 5000000
#define MAX_DATA_VALUE 2800000
#define NUM_BINS 15  // You can adjust the number of bins as needed

int main() {

    // Assuming each line in the file contains one integer
    int item;

    int index = 0;


    int *data;  // Assuming your data is stored in an array
    data = (int *)malloc(DATA_SIZE * sizeof(int));


    // Open the file for reading
    FILE *file = fopen("new_moderate.csv", "r");


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

    int histogram[NUM_BINS] = {0}; // Initialize histogram bins to zero

    char fname[15][10]; 

    FILE * fdbin[15];
    for(int cnt=0; cnt<15; cnt++){
        sprintf(fname[cnt], "mbin%d", cnt);
    	fdbin[cnt] = fopen(fname[cnt],"w");
    	if (fdbin[cnt] == NULL) {
        	perror("Error opening file");
        	return 1;
    	}
    }



    // Calculate the histogram
    for (int i = 0; i < DATA_SIZE; i++) {
        int bin = (data[i] * NUM_BINS) / MAX_DATA_VALUE;  // Adjust the range if needed
        if (bin >= 0 && bin < NUM_BINS) {
            histogram[bin]++;           
            fprintf(fdbin[bin], "%d\n", data[i]);
        }
    }

    for(int cnt=0; cnt<15; cnt++)
	fclose(fdbin[cnt]);


    file = fopen("new_moderate_bins.csv", "w");


    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }


    // Print the histogram
    for (int i = 0; i < NUM_BINS; i++) {
        fprintf(file, "%d\n", histogram[i]);
    //  printf("Bin %d: %d\n", i, histogram[i]);
    }

    fclose(file);

    return 0;
}
