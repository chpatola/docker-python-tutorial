# Tutorial for using Docker with python

In this tutorial, base data is read from an Azure container, a column is added and the dataframe is then written to another container. The code is run in Docker.

### Installation Instructions

1. Install docker: https://docs.docker.com/get-docker/
2. Add sudo to your docker group: https://docs.docker.com/engine/install/linux-postinstall/
3. Clone this repo to your machine
4. Create an .env file in the root directory where you insert the SAS URL*:s to the input file (URL_TO_INPUT_BLOB) and the output container (URL_TO_OUTPUT_CONTAINER). Use the format KEY=VALUE (no quotation marks)
5. If you have not already, cd into the root directory. 
6. Build the image:```docker image build . -t <the_name_you_want_to_give_the_image>```

### Useage instructions
 Run the container from the image: ```docker run --env-file .env -it -v "$(pwd):/usr/src/handle_data" --name <the_name_you_want_to_give_the_container> <image_name>```
 
 
 **In Azure Storage Account, you find the SAS URL:s by left clicking on the file/container and choosing "Generate SAS". Make sure you give the access for long enough time and tick all rights you need (read, write..).*
