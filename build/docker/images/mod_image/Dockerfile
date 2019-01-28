FROM cent76_conda3

ENV PORT 8080

COPY scripts /opt/scripts

RUN chmod +x /opt/scripts/*.sh \
    && echo "export PORT=8080" >> ~/.bashrc

EXPOSE 8080

WORKDIR /opt/scripts

ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

