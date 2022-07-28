FROM facthunder/cppcheck:latest

ADD ./src/main.py /main.py

VOLUME ["/home/test"]

ENTRYPOINT ["python", "/main.py"]