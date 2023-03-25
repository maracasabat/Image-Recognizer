

if (document.getElementById("my-awesome-dropzone")) {
    Dropzone.autoDiscover = false;
    const myDropzone = new Dropzone("#my-awesome-dropzone", {
        url: "upload/",
        maxFiles: 1,
        maxFilesize: 2,
        acceptedFiles: "image/*",
});
}