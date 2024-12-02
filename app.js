// Клас для звичайного телефону
var BasicPhone = /** @class */ (function () {
    function BasicPhone() {
    }
    BasicPhone.prototype.makeCall = function () {
        console.log("Здійснення голосового виклику через телефон.");
    };
    return BasicPhone;
}());
// Клас для відео камери
var VideoCamera = /** @class */ (function () {
    function VideoCamera() {
    }
    VideoCamera.prototype.startVideoCall = function () {
        console.log("Відео дзвінок через камеру.");
    };
    return VideoCamera;
}());
// Адаптер для інтеграції відео камери до інтерфейсу Phone
var VideoCallAdapter = /** @class */ (function () {
    function VideoCallAdapter(videoCamera) {
        this.videoCamera = videoCamera;
    }
    VideoCallAdapter.prototype.makeCall = function () {
        this.videoCamera.startVideoCall();
    };
    return VideoCallAdapter;
}());
// Функція для демонстрації викликів
function demoCall(phone) {
    phone.makeCall();
}
// Додавання подій до інтерфейсу
document.addEventListener("DOMContentLoaded", function () {
    var voiceCallBtn = document.getElementById("voiceCallBtn");
    var videoCallBtn = document.getElementById("videoCallBtn");
    // Звичайний голосовий виклик
    var basicPhone = new BasicPhone();
    // Відео виклик через адаптер
    var videoPhone = new VideoCallAdapter(new VideoCamera());
    // Події для кнопок
    voiceCallBtn.addEventListener("click", function () { return demoCall(basicPhone); });
    videoCallBtn.addEventListener("click", function () { return demoCall(videoPhone); });
});
