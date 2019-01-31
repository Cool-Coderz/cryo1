FROM cent76_conda3_django194

COPY scripts /opt/scripts

RUN chmod +x /opt/scripts/*.sh \
    && mkdir -p /opt/django

EXPOSE 8000

WORKDIR /opt/scripts

ENTRYPOINT ["/opt/scripts/entrypoint.sh"]
