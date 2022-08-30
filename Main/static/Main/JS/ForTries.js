"use strict"

function jsFunk() {
    return "String For Java Script Outs";
}

function stringsWithTheFor() {
    let str = '';
    for (let i = 0; i < 5; i++) {
        str += 'str №' + String(i + 1) + '<br \/>';
    }
return str;
}



class FramePerSomething {
    constructor(fps) {
        this.fps = fps;
        this.max_timer = 3500;
        this.max_opacity = 100;
    }

    makeOpacityStep() {
        return Math.floor(this.max_opacity / this.fps);
    }

    makeTimersStep() {
        return Math.floor(this.max_timer / this.fps);
    }


}

let enter_of_fps = 100; /* Good value is 50 or can be 20,25,100 */

let fps = new FramePerSomething(enter_of_fps);

function minusOpacityByTime (frame_rate=enter_of_fps) {
    let all_values_of_opacity = 100
    let all_values_of_timers = 0

    for (let i = 0; i < frame_rate; i++) {
        all_values_of_opacity -= fps.makeOpacityStep();
        all_values_of_timers += fps.makeTimersStep();
        (function () {
            let all_values_of_opacity_2 = all_values_of_opacity;
            let all_values_of_timers_2 = all_values_of_timers;
            let error1 = "Your nums is string or negative. Maybe float mums have more, then 2 symbols after (. or ,). "+
                "Or nums can have 0 ahead integer value. ("
            if ((parseFloat(moveComma(all_values_of_opacity_2, -2)) ===
                (moveComma(all_values_of_opacity_2, -2))) &&
                (Number.isInteger(all_values_of_timers_2))) {

                return setTimeout(() => {
                    document.getElementById('NeedToHideByJS').style.opacity =
                    moveComma(all_values_of_opacity_2, -2)}, all_values_of_timers_2);

            } else {
                return console.log(error1 += String(i));
            }
        })()
    }
}

function moveComma(val, moveCommaByInput) {
    if (val || typeof val === 'number') {
        const valueNumber = Number(val);
        const moveCommaBy = moveCommaByInput || 0;

            if (isNaN(valueNumber)) {
                return null;
            } else {
                return Number(`${valueNumber}e${moveCommaBy}`);
            }
    }

    return null;
}

let JS_Try_Mode_Output = stringsWithTheFor();
