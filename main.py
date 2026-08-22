

from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width,
                   initial-scale=1.0,
                   maximum-scale=1.0,
                   user-scalable=no,
                   viewport-fit=cover">

    <meta name="apple-mobile-web-app-capable"
          content="yes">

    <meta name="mobile-web-app-capable"
          content="yes">

    <title>Wish ♡</title>


    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }


        html,
        body {

            width: 100%;
            height: 100%;

            overflow: hidden;

            margin: 0;
            padding: 0;

            background: #000;
        }


        body {

            min-height: 100dvh;

            background-image:
                url("/bgs/bg1.jpg");

            background-size: cover;

            background-position: center;

            background-repeat: no-repeat;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            position: relative;

            -webkit-tap-highlight-color:
                transparent;

            -webkit-user-select: none;

            user-select: none;

            touch-action: manipulation;
        }


        /* =====================================
           ЛЕГКЕ ЗАТЕМНЕННЯ
           ===================================== */

        body::before {

            content: "";

            position: fixed;

            inset: 0;

            background:
                rgba(0, 0, 0, 0.08);

            z-index: 0;

            pointer-events: none;
        }


        /* =====================================
           START SCREEN
           ===================================== */

        #startScreen {

            position: fixed;

            inset: 0;

            width: 100%;
            height: 100%;

            min-height: 100dvh;

            display: flex;

            flex-direction: column;

            justify-content: center;

            align-items: center;

            padding:
                env(safe-area-inset-top)
                env(safe-area-inset-right)
                env(safe-area-inset-bottom)
                env(safe-area-inset-left);

            z-index: 2;
        }


        /* =====================================
           ГОЛОВНА КНОПКА
           ===================================== */

        #wishButton {

            position: relative;

            width: min(720px, 82vw);

            cursor: pointer;

            display: block;

            flex-shrink: 0;

            transition:
                transform 0.2s ease,
                opacity 0.35s ease;
        }


        #wishButton:active {

            transform:
                scale(0.94);
        }


        #wishButton img {

            width: 100%;

            height: auto;

            display: block;
        }


        /* =====================================
           ТЕКСТ НА ГОЛОВНІЙ КНОПЦІ
           ===================================== */

        #buttonText {

            position: absolute;

            left: 50%;
            top: 50%;

            transform:
                translate(-50%, -50%);

            width: 78%;

            color: white;

            font-size:
                clamp(13px, 4vw, 21px);

            font-weight: 800;

            line-height: 1.1;

            text-align: center;

            pointer-events: none;

            text-shadow:
                1px 1px 3px #9e2164;
        }


        /* =====================================
           INST
           ===================================== */

        #instagram {

            margin-top: 12px;

            width: 90%;

            color: white;

            font-size:
                clamp(14px, 4vw, 20px);

            font-weight: 800;

            line-height: 1.2;

            text-align: center;

            text-shadow:
                1px 1px 4px #9e2164;

            pointer-events: none;
        }


        /* =====================================
           SOUND BUTTON
           ===================================== */

        #soundButton {

            position: fixed;

            top:
                calc(
                    8px +
                    env(safe-area-inset-top)
                );

            right:
                calc(
                    8px +
                    env(safe-area-inset-right)
                );

            width: clamp(70px, 23vw, 116px);

            height: clamp(70px, 23vw, 116px);

            cursor: pointer;

            z-index: 20;

            transition:
                transform 0.2s ease;
        }


        #soundButton:active {

            transform:
                scale(0.9);
        }


        #soundButton img {

            width: 100%;
            height: 100%;

            object-fit: contain;

            display: block;
        }


        #soundText {

            position: absolute;

            left: 50%;
            top: 50%;

            transform:
                translate(-50%, -50%);

            width: 80%;

            color: white;

            font-size:
                clamp(13px, 4vw, 20px);

            font-weight: 800;

            line-height: 1;

            text-align: center;

            pointer-events: none;

            text-shadow:
                1px 1px 3px #9e2164;
        }


        /* =====================================
           RESULT SCREEN
           ===================================== */

        #resultScreen {

            position: fixed;

            inset: 0;

            width: 100%;
            height: 100%;

            min-height: 100dvh;

            display: none;

            flex-direction: column;

            align-items: center;

            z-index: 2;

            padding-top:
                max(
                    16vh,
                    calc(
                        50px +
                        env(safe-area-inset-top)
                    )
                );

            padding-left: 20px;

            padding-right: 20px;

            overflow: hidden;

            animation:
                appear 0.6s ease;
        }


        /* =====================================
           BACK BUTTON
           ===================================== */

        #backButton {

            position: fixed;

            top:
                calc(
                    3px +
                    env(safe-area-inset-top)
                );

            left:
                calc(
                    8px +
                    env(safe-area-inset-left)
                );

            width: clamp(70px, 23vw, 116px);

            height: clamp(70px, 23vw, 116px);

            cursor: pointer;

            z-index: 20;

            transition:
                transform 0.2s ease;
        }


        #backButton:active {

            transform:
                scale(0.9);
        }


        #backButton img {

            width: 100%;
            height: 100%;

            object-fit: contain;

            display: block;
        }


        #backArrow {

            position: absolute;

            left: 50%;
            top: 45%;

            transform:
                translate(-50%, -50%);

            color: white;

            font-size:
                clamp(28px, 9vw, 45px);

            font-weight: 900;

            line-height: 1;

            pointer-events: none;

            text-shadow:
                1px 1px 3px #9e2164;
        }


        /* =====================================
           PICTURE
           ===================================== */

        #wishPicture {

            width:
                min(68vw, 280px);

            max-width: 90vw;

            max-height: 35vh;

            object-fit: contain;

            border-radius: 10px;

            display: block;

            flex-shrink: 1;

            filter:
                drop-shadow(
                    0 5px 12px
                    rgba(0,0,0,0.25)
                );

            animation:
                pictureAppear
                0.7s ease;
        }


        /* =====================================
           QUOTE
           ===================================== */

        #quote {

            width:
                min(88vw, 430px);

            max-width: 90vw;

            margin-top: 18px;

            color: white;

            font-size:
                clamp(15px, 4.8vw, 21px);

            font-weight: 800;

            line-height: 1.3;

            text-align: center;

            text-shadow:
                1px 1px 4px #9e2164;

            animation:
                quoteAppear
                0.8s ease;
        }


        /* =====================================
           HEART BUTTON
           ===================================== */

        #heartButton {

            position: relative;

            width:
                min(260px, 65vw);

            margin-top: 22px;

            cursor: pointer;

            flex-shrink: 0;

            transition:
                transform 0.2s ease;

            animation:
                quoteAppear
                1s ease;
        }


        #heartButton:active {

            transform:
                scale(0.94);
        }


        #heartButton img {

            width: 100%;

            height: auto;

            display: block;
        }


        #heartText {

            position: absolute;

            left: 50%;
            top: 50%;

            transform:
                translate(-50%, -50%);

            width: 82%;

            color: white;

            font-size:
                clamp(14px, 4vw, 19px);

            font-weight: 800;

            line-height: 1.1;

            text-align: center;

            pointer-events: none;

            text-shadow:
                1px 1px 3px #9e2164;
        }


        /* =====================================
           SOUND MENU
           ===================================== */

        #soundMenu {

            position: fixed;

            inset: 0;

            display: none;

            justify-content: center;

            align-items: center;

            z-index: 100;

            padding:
                env(safe-area-inset-top)
                env(safe-area-inset-right)
                env(safe-area-inset-bottom)
                env(safe-area-inset-left);

            animation:
                soundMenuAppear
                0.35s ease;
        }


        #soundBlur {

            position: absolute;

            inset: 0;

            background:
                rgba(0, 0, 0, 0.18);

            backdrop-filter:
                blur(12px);

            -webkit-backdrop-filter:
                blur(12px);
        }


        #soundPanel {

            position: relative;

            z-index: 101;

            width:
                min(82vw, 400px);

            display: flex;

            flex-direction: column;

            align-items: center;

            justify-content: center;
        }


        /* =====================================
           VOLUME SLIDER
           ===================================== */

        #volumeSlider {

            width:
                min(72vw, 320px);

            height: 10px;

            appearance: none;

            -webkit-appearance: none;

            background: white;

            border-radius: 10px;

            outline: none;

            cursor: pointer;

            box-shadow:
                0 2px 8px
                rgba(0,0,0,0.25);
        }


        #volumeSlider::-webkit-slider-thumb {

            appearance: none;

            -webkit-appearance: none;

            width: 30px;

            height: 30px;

            border-radius: 50%;

            background: #9e2164;

            border: 3px solid white;

            cursor: pointer;

            box-shadow:
                0 2px 6px
                rgba(0,0,0,0.3);
        }


        #volumeSlider::-moz-range-thumb {

            width: 30px;

            height: 30px;

            border-radius: 50%;

            background: #9e2164;

            border: 3px solid white;

            cursor: pointer;

            box-shadow:
                0 2px 6px
                rgba(0,0,0,0.3);
        }


        /* =====================================
           EXIT SOUND
           ===================================== */

        #exitSoundButton {

            position: relative;

            width:
                min(220px, 55vw);

            margin-top: 35px;

            cursor: pointer;

            transition:
                transform 0.2s ease;
        }


        #exitSoundButton:active {

            transform:
                scale(0.94);
        }


        #exitSoundButton img {

            width: 100%;

            height: auto;

            display: block;
        }


        #exitSoundText {

            position: absolute;

            left: 50%;
            top: 50%;

            transform:
                translate(-50%, -50%);

            width: 80%;

            color: white;

            font-size:
                clamp(16px, 5vw, 22px);

            font-weight: 800;

            text-align: center;

            pointer-events: none;

            text-shadow:
                1px 1px 3px #9e2164;
        }


        /* =====================================
           ANIMATIONS
           ===================================== */

        @keyframes appear {

            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }


        @keyframes pictureAppear {

            from {

                opacity: 0;

                transform:
                    translateY(15px)
                    scale(0.92);
            }

            to {

                opacity: 1;

                transform:
                    translateY(0)
                    scale(1);
            }
        }


        @keyframes quoteAppear {

            from {

                opacity: 0;

                transform:
                    translateY(10px);
            }

            to {

                opacity: 1;

                transform:
                    translateY(0);
            }
        }


        @keyframes soundMenuAppear {

            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }


        /* =====================================
           ДУЖЕ НИЗЬКИЙ ЕКРАН
           ===================================== */

        @media (max-height: 650px) {

            #resultScreen {

                padding-top: 11vh;
            }


            #wishPicture {

                max-height: 30vh;

                width:
                    min(60vw, 230px);
            }


            #quote {

                margin-top: 12px;

                font-size:
                    clamp(14px, 4vw, 17px);
            }


            #heartButton {

                width:
                    min(210px, 55vw);

                margin-top: 14px;
            }
        }


        /* =====================================
           ДУЖЕ ВУЗЬКИЙ ТЕЛЕФОН
           ===================================== */

        @media (max-width: 360px) {

            #wishPicture {

                width: 62vw;

                max-height: 29vh;
            }


            #quote {

                font-size: 15px;

                width: 92%;
            }


            #heartButton {

                width: 200px;

                margin-top: 14px;
            }


            #heartText {

                font-size: 15px;
            }
        }

    </style>

</head>


<body>


    <!-- =====================================
         BACKGROUND MUSIC
         ===================================== -->

    <audio
        id="backgroundMusic"
        src="/sounds/bgn1.mp3"
        loop
        preload="auto">
    </audio>


    <!-- =====================================
         CLICK SOUND
         ===================================== -->

    <audio
        id="clickSound"
        src="/sounds/click1.mp3"
        preload="auto">
    </audio>


    <!-- =====================================
         SOUND BUTTON
         ===================================== -->

    <div id="soundButton">

        <img
            src="/btns/bt1.png"
            alt="Sound">

        <div id="soundText">
            sound
        </div>

    </div>


    <!-- =====================================
         START
         ===================================== -->

    <div id="startScreen">


        <div id="wishButton">

            <img
                src="/btns/bt1.png"
                alt="Click for the wish">

            <div id="buttonText">
                click for the wish
            </div>

        </div>


        <div id="instagram">
            inst: himkaqxx
        </div>


    </div>


    <!-- =====================================
         RESULT
         ===================================== -->

    <div id="resultScreen">


        <!-- BACK -->

        <div id="backButton">

            <img
                src="/btns/bt1.png"
                alt="Back">

            <div id="backArrow">
                ←
            </div>

        </div>


        <!-- PICTURE -->

        <img
            id="wishPicture"
            src=""
            alt="Your wish">


        <!-- QUOTE -->

        <div id="quote"></div>


        <!-- HEART -->

        <div id="heartButton">

            <img
                src="/btns/bt1.png"
                alt="Give me a heart">

            <div id="heartText">
                give me a heart
            </div>

        </div>


    </div>


    <!-- =====================================
         SOUND MENU
         ===================================== -->

    <div id="soundMenu">


        <div id="soundBlur"></div>


        <div id="soundPanel">


            <input
                id="volumeSlider"
                type="range"
                min="0"
                max="1"
                step="0.01"
                value="0.35">


            <div id="exitSoundButton">

                <img
                    src="/btns/bt1.png"
                    alt="Exit">

                <div id="exitSoundText">
                    exit
                </div>

            </div>


        </div>

    </div>


    <script>


        /* =====================================
           AUDIO
           ===================================== */

        const backgroundMusic =
            document.getElementById(
                "backgroundMusic"
            );


        const clickSound =
            document.getElementById(
                "clickSound"
            );


        const volumeSlider =
            document.getElementById(
                "volumeSlider"
            );


        backgroundMusic.volume = 0.35;

        clickSound.volume = 0.35;


        /* =====================================
           START MUSIC
           
           На iPhone Safari autoplay
           може бути заблокований.
           Після першого дотику
           музика запускається.
           ===================================== */

        function startMusic() {

            backgroundMusic.volume =
                parseFloat(
                    volumeSlider.value
                );


            backgroundMusic
                .play()
                .catch(function() {

                    console.log(
                        "Autoplay blocked"
                    );

                });
        }


        window.addEventListener(
            "load",
            function() {

                startMusic();

            }
        );


        document.addEventListener(
            "touchstart",
            function() {

                startMusic();

            },
            {
                once: true,
                passive: true
            }
        );


        document.addEventListener(
            "click",
            function() {

                startMusic();

            },
            {
                once: true
            }
        );


        /* =====================================
           CLICK SOUND
           ===================================== */

        function playClickSound() {

            clickSound.currentTime = 0;

            clickSound.volume =
                parseFloat(
                    volumeSlider.value
                );


            clickSound
                .play()
                .catch(function() {

                    console.log(
                        "Click sound blocked"
                    );

                });
        }


        /* =====================================
           SOUND MENU
           ===================================== */

        const soundButton =
            document.getElementById(
                "soundButton"
            );


        const soundMenu =
            document.getElementById(
                "soundMenu"
            );


        const exitSoundButton =
            document.getElementById(
                "exitSoundButton"
            );


        soundButton.addEventListener(
            "click",
            function() {

                playClickSound();

                soundMenu.style.display =
                    "flex";
            }
        );


        /* =====================================
           VOLUME
           
           Керує ОБОМА звуками
           ===================================== */

        volumeSlider.addEventListener(
            "input",
            function() {

                const volume =
                    parseFloat(
                        volumeSlider.value
                    );


                backgroundMusic.volume =
                    volume;


                clickSound.volume =
                    volume;

            }
        );


        /* =====================================
           EXIT SOUND MENU
           ===================================== */

        exitSoundButton.addEventListener(
            "click",
            function() {

                playClickSound();

                soundMenu.style.display =
                    "none";

            }
        );


        /* =====================================
           PICTURES
           
           Якщо у тебе більше/менше картинок,
           просто зміни цей список.
           ===================================== */

        const pictures = [

            "/pictures/p1.jpg",

            "/pictures/p2.jpg",

            "/pictures/p3.jpg",

            "/pictures/p4.jpg",

            "/pictures/p5.jpg",

            "/pictures/p6.jpg",

            "/pictures/p7.jpg",

            "/pictures/p8.jpg",

            "/pictures/p9.jpg",

            "/pictures/p10.jpg",

            "/pictures/p11.jpg",

            "/pictures/p12.jpg",

            "/pictures/p13.jpg",

            "/pictures/p14.jpg",

            "/pictures/p15.jpg",

            "/pictures/p16.jpg",

            "/pictures/p17.jpg",

            "/pictures/p18.jpg"

        ];


        /* =====================================
           QUOTES
           ===================================== */

        const quotes = [

            "May your day be as bright as the morning sun♡",

            "I hope you face the next twenty-four hours with a calm mind and a joyful heart♡",

            "May today bring you small wins, big laughs, and wonderful surprises♡",

            "Wishing you the strength to handle any challenge and the peace to enjoy every quiet moment♡",

            "May your coffee be strong, your tasks be easy, and your mood be cheerful♡",

            "Here is to a day full of fresh energy, new opportunities, and kind people♡",

            "May you feel appreciated, supported, and never alone in whatever you do today♡",

            "I hope your thoughts stay positive and your steps stay light♡",

            "May today bring you closer to your biggest goals and your happiest dreams♡",

            "Have a wonderful day filled with love♡",

            "May your day be filled with good music, great coffee, and zero stress♡",

            "Take a deep breath, smile, and own the day♡",

            "Wishing you a cozy, beautiful, and completely stress-free day♡",

            "May your heart be light and your day be extra sweet♡",

            "Sending a pocketful of sunshine straight to you♡",

            "Hope you feel appreciated, special, and loved today♡",

            "May every moment of today bring a smile to your face♡",

            "Go get 'em! You are going to do amazing things today♡",

            "Wishing you a smooth, happy, and wonderful day from start to finish♡",

            "May your day be as wonderful as you are!♡"

        ];


        /* =====================================
           ELEMENTS
           ===================================== */

        const startScreen =
            document.getElementById(
                "startScreen"
            );


        const resultScreen =
            document.getElementById(
                "resultScreen"
            );


        const wishButton =
            document.getElementById(
                "wishButton"
            );


        const backButton =
            document.getElementById(
                "backButton"
            );


        const wishPicture =
            document.getElementById(
                "wishPicture"
            );


        const quote =
            document.getElementById(
                "quote"
            );


        const heartButton =
            document.getElementById(
                "heartButton"
            );


        let lastPicture = -1;

        let lastQuote = -1;


        /* =====================================
           RANDOM WITHOUT IMMEDIATE REPEAT
           ===================================== */

        function getRandomIndex(
            length,
            lastIndex
        ) {

            if (length <= 1) {

                return 0;
            }


            let index;


            do {

                index =
                    Math.floor(
                        Math.random() * length
                    );

            }
            while (
                index === lastIndex
            );


            return index;
        }


        /* =====================================
           SHOW WISH
           ===================================== */

        function showWish() {

            playClickSound();

            startMusic();


            const pictureIndex =
                getRandomIndex(
                    pictures.length,
                    lastPicture
                );


            lastPicture =
                pictureIndex;


            const quoteIndex =
                getRandomIndex(
                    quotes.length,
                    lastQuote
                );


            lastQuote =
                quoteIndex;


            wishPicture.src =
                pictures[pictureIndex];


            quote.textContent =
                quotes[quoteIndex];


            startScreen.style.display =
                "none";


            resultScreen.style.display =
                "flex";


            /* Restart animations */

            wishPicture.style.animation =
                "none";

            quote.style.animation =
                "none";

            heartButton.style.animation =
                "none";


            void wishPicture.offsetWidth;

            void quote.offsetWidth;

            void heartButton.offsetWidth;


            wishPicture.style.animation =
                "pictureAppear 0.7s ease";


            quote.style.animation =
                "quoteAppear 0.8s ease";


            heartButton.style.animation =
                "quoteAppear 1s ease";
        }


        /* =====================================
           BACK
           ===================================== */

        function goBack() {

            playClickSound();


            resultScreen.style.display =
                "none";


            startScreen.style.display =
                "flex";
        }


        /* =====================================
           BUTTONS
           ===================================== */

        wishButton.addEventListener(
            "click",
            showWish
        );


        backButton.addEventListener(
            "click",
            goBack
        );


        /* =====================================
           GIVE ME A HEART
           
           Зараз кнопка просто виконує
           дію/звук.
           
           Справжні push-повідомлення
           потребують окремої Web Push
           системи та HTTPS.
           ===================================== */

        heartButton.addEventListener(
            "click",
            function() {

                playClickSound();

                alert("♡");

            }
        );


    </script>

</body>

</html>
"""


# ==========================================
# MAIN PAGE
# ==========================================

@app.route("/")
def home():

    return render_template_string(
        HTML
    )


# ==========================================
# BACKGROUNDS
# ==========================================

@app.route("/bgs/<path:filename>")
def bgs(filename):

    return send_from_directory(
        "bgs",
        filename
    )


# ==========================================
# BUTTONS
# ==========================================

@app.route("/btns/<path:filename>")
def btns(filename):

    return send_from_directory(
        "btns",
        filename
    )


# ==========================================
# PICTURES
# ==========================================

@app.route("/pictures/<path:filename>")
def pictures(filename):

    return send_from_directory(
        "pictures",
        filename
    )


# ==========================================
# SOUNDS
# ==========================================

@app.route("/sounds/<path:filename>")
def sounds(filename):

    return send_from_directory(
        "sounds",
        filename
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )



