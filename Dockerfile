FROM facthunder/cppcheck

ADD ./src/main.py /main.py

VOLUME ["/home/test"]

ENTRYPOINT ["python", "/main.py"]