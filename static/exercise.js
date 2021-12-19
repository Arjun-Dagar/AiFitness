document.getElementById("bicep-start").addEventListener("click", function () {
    document.getElementById("jo-change-karni-hai").classList.toggle("webcam-outlet");
    document.getElementById("jo-change-karni-hai").classList.toggle("webcam-outlet-change");
    document.getElementById("jo-change-karni-hai").src = "{{ url_for('video') }}";
    document.getElementById("close").style.zIndex = "200";
});

document.getElementById("close").addEventListener("click", function () {
    document.getElementById("jo-change-karni-hai").classList.toggle("webcam-outlet");
    document.getElementById("jo-change-karni-hai").classList.toggle("webcam-outlet-change");
    document.getElementById("jo-change-karni-hai").src = "";
    document.getElementById("close").style.zIndex = "-1";
});

