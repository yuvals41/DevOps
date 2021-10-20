FROM ubuntu
WORKDIR /opt/
RUN sudo apt update
RUN sudo apt install python3.9
COPY C:\Users\yuval\Desktop\Python projects\liorBFF.py /opt/
EXPOSE 5000
ENTRYPOINT ["python","/opt/liorBFF.py"]