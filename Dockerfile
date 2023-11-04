# Use Ubuntu as the base image
#Specify the base image as Ubuntu.
FROM ubuntu:latest
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Create a directory inside the container at /home/doc-bd-a1/
RUN mkdir -p /home

#Install the following packages in the Dockerfile: Python3, Pandas, Numpy, Seaborn, Matplotlib, scikit-learn, and Scipy.
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y python3 python3-pip

# Install Python packages using pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Copies a dataset file named dataset.csv from your local machine to the /home/doc-bd-a1/directory within the container.
# Move the dataset file to the container.
# (copies the local file C:/file.txt to the /home directory of the container)
COPY dataset.csv /home/doc-bd-a1/




# Specify the command to run when the container is launched

CMD ["/bin/bash"]




