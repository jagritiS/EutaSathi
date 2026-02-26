function ask() {


    const text = document.getElementById("question").value;

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("answer_en").innerText = data.answer_en;
        document.getElementById("answer_np").innerText = data.answer_np;

        const box = document.getElementById("riskBox");
        box.style.display = "block";
        box.className = "risk " + data.risk;
        box.innerText = data.risk === "red"
            ? "⚠ High Risk"
            : "✅ Normal Guidance";
    });
}

// Voice input
function startVoice() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.onresult = function(event) {
        document.getElementById("question").value =
            event.results[0][0].transcript;
    };
    recognition.start();
}
function speak(lang) {
    let text = "";
    let voiceLang = "en-US"; // default

    if(lang === "en") {
        text = document.getElementById("answer_en").innerText;
        voiceLang = "en-US";
    } else if(lang === "np") {
        text = document.getElementById("answer_np").innerText;
        voiceLang = "hi-IN"; // Nepali
    }

    if('speechSynthesis' in window) {
        const utter = new SpeechSynthesisUtterance(text);
        utter.lang = voiceLang;
        window.speechSynthesis.speak(utter);
    } else {
        alert("Sorry, your browser does not support text-to-speech.");
    }
}

