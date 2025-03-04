    // When the modal is hidden (closed), stop the video
    $('#videoModal').on('hidden.bs.modal', function () {
        var video = document.getElementById('videoPlayer');
        video.pause();  // Pause the video
        video.currentTime = 0;  // Reset video to the start
    });
