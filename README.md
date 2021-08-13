# Prepare the Dockerfile

- Please note that Dockerfile always starts with a default image called base-image, examples include things like a tomcat, red hat image or an Ubuntu base-image.
 This is the building block for our image, this image band can be expanded to as lean as you would like, as we can add things to this image or build “layers”.

- As mentioned above, the current docker image is built with a simple Dockerfile that uses a tomcat base-image from the official Apache Tomcat repository. To make our base image Ubuntu, add this line with the:

FROM tomcat:8.0-jre8

#### The next step

Now we need to remove all the pre-installed webapps by using a command RUN rm.
Dockerfile removes all pre-installed webapps from tomcat and copies the WEKA Rest service war file to /usr/local/tomcat/webapps/ROOT.war as the main application.

We shall run our application on port 8080. To do that lets use the docker EXPOSE command to open up that port as: 

EXPOSE 8080

The final Dockerfile should look like this:
FROM tomcat:8.0-jre8
MAINTAINER "Moses <abc@gmail.com>"

 --- remove preinstalled webapps 
RUN rm -fr /usr/local/tomcat/webapps/ROOT
RUN rm -fr /usr/local/tomcat/webapps/host-manager
RUN rm -fr /usr/local/tomcat/webapps/manager
RUN rm -fr /usr/local/tomcat/webapps/docs
RUN rm -fr /usr/local/tomcat/webapps/examples

COPY target/weka_sqa-1.0war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080

You can customize the Dockerfile as needed for example changing the maintainer name and email address, Specify the war filename and the version corresponding to the changes in the pom.xml

## Build the Docker Image
### Set up the project
- 	Using commend navigate to the directory where you would like to the project source code from Github and type in the command bellow:
git clone https://github.com/openjamoses/weka_rest_version.git
- 	Navigate to the project directory you have just cloned:
cd wekarest
- 	Compile the war (Web Application Archive) file with maven
mvn clean package
- 	To build the docker image with the weka_sqa
            docker build . -t weka_sqa
- 	You can go ahead and verify that image built correctly with:
docker images 
- 	Now, let’s bring up a container called weka_sqa_container which will be based on the image weka_sqa using the docker command.
docker run -t -p 8080:8080 --name weka_sqa_container weka_sqa

To run the container in the background, add -d to your docker run command. 
Use ctrl + c to exit the container. 
Now use the command docker ps -a. to view your container
Showing you the URL link, you can assess the page as:
0.0.0.0:8080

### Tag your Image** 
First, list the image and find the one you built. Next, tag the image by using the image id (my id is: 5ua43ad124rf2) and tagging it with your docker username a name of your choice. My docker username is username and the name we tag it with is username /weka sqa_image:1.0 . Make sure you specify the tag name and tag version, separated by a colon (:).
docker tag 5ua43ad124rf2 username /weka_sqa_image:1.0 

### Push the image to the public Docker Hub**
- Use the same name you used to tag the image:
- docker push username/weka_sqa_image:1.0 
