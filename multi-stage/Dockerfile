# `scratch` just means there is no base image, as in we're creating an image
# "from scratch." This is a non-normative example.
FROM scratch AS src
COPY important.txt /data/

FROM nginx AS production
# Copy from the `src` stage (above) the `important.txt` file to the nginx image
# here at `/data/important.txt`.
COPY --from=src /data/important.txt /data/
COPY default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx"]