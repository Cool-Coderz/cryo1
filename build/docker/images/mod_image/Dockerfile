FROM cent76_conda3

ENV PORT 8000

COPY scripts /opt/scripts

RUN chmod +x /opt/scripts/*.sh \
    && echo "export PORT=8000" >> ~/.bashrc

EXPOSE 8000

WORKDIR /opt/scripts

ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

