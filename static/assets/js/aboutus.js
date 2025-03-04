$(".box-aboutus") .click (function () {
    $ (".box-aboutus") .removeClass ("aboutus-active");
    $ (this) .addClass ("aboutus-active");
});







document.querySelectorAll('video').forEach(video => {
  video.addEventListener('click', function () {
    if (this.paused) {
      this.play(); 
      this.muted = false; 
    } else {
      this.pause(); 
    }
  });
});