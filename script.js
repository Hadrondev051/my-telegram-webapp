let tg = window.Telegram.WebApp;
tg.expand(); // صفحه رو بزرگ کن

function sendData() {
    tg.sendData("دکمه کلیک شد! 🎉");
    tg.close(); // بعد از ارسال ببند
}