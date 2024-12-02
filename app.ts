
interface Phone {
    makeCall(): void; 
}


class BasicPhone implements Phone {
    makeCall(): void {
        console.log("Здійснення голосового виклику через телефон.");
    }
}


class VideoCamera {
    startVideoCall(): void {
        console.log("Відео дзвінок через камеру.");
    }
}


class VideoCallAdapter implements Phone {
    private videoCamera: VideoCamera;

    constructor(videoCamera: VideoCamera) {
        this.videoCamera = videoCamera;
    }

    makeCall(): void {
        this.videoCamera.startVideoCall();
    }
}

function demoCall(phone: Phone): void {
    phone.makeCall();
}


document.addEventListener("DOMContentLoaded", () => {
    const voiceCallBtn = document.getElementById("voiceCallBtn")!;
    const videoCallBtn = document.getElementById("videoCallBtn")!;

    
    const basicPhone = new BasicPhone();

    
    const videoPhone = new VideoCallAdapter(new VideoCamera());

   
    voiceCallBtn.addEventListener("click", () => demoCall(basicPhone));
    videoCallBtn.addEventListener("click", () => demoCall(videoPhone));
});
