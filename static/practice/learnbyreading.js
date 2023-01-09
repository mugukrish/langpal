
function readforme(){
    const synth = window.speechSynthesis;
    const utterThis = new SpeechSynthesisUtterance(document.getElementById("toread").value);
    synth.speak(utterThis);

}

function clearread(){
    document.getElementById("result").innerHTML =""
}

const button = document.getElementById("button_sel");
const result = document.getElementById("result");
console.log(button, result)

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if(SpeechRecognition){

    let speechRecognition = new webkitSpeechRecognition();
    let listening = false;

    const start = () => {
        console.log("came to start")
        speechRecognition.start();
        button.textContent = "Stop listening";
    };

    const stop = () => {
        speechRecognition.stop();
        button.textContent = "Start";

    };

    const onResult = event => {
    result.innerHTML = "";
    for (const res of event.results) {
        const text = document.createTextNode(res[0].transcript);
        const p = document.createElement("p");
        if (res.isFinal) {
        p.classList.add("final");
        }
        p.appendChild(text);
        result.appendChild(p);
    }
    }

    speechRecognition.continuous = true;
    speechRecognition.interimResults = true;
    speechRecognition.addEventListener("result", onResult);

    button.addEventListener("click", () => {
        listening ? stop() : start();
        listening = !listening;
      });

}

else{
    console.log("Not Supported");
}