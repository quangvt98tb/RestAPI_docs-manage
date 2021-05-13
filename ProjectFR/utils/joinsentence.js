
export const joinSen = list_word => {
    // join array
    let sentence = "";
    for (let i = 0; i < list_word.length; i++) {
        let element = list_word[i];
        if (element["type"] == 1) {
            sentence = sentence + element["word"];
        } else if (element["type"] == 0) {
            sentence = sentence + element["word"] + " ";
        }
    }

    // remove <>
    let text_fix = sentence;
    const daucau = ".,;?:!";
    for (let i = 0; i < daucau.length; i++) {
        let i_tag = " <" + daucau[i] + ">";
        let idx = text_fix.search(i_tag);
        if (idx == -1) {
            text_fix = text_fix;
        } else {
            text_fix = text_fix.split(i_tag).join(daucau[i] + ' ');
        }
    }
    return text_fix
}
