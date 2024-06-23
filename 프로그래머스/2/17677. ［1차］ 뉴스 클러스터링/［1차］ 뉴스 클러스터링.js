function solution(str1, str2) {
    const str1Arr = sliceString(str1);
    const str2Arr = sliceString(str2);
    let gyo = [];
    let hap = str1Arr.concat(str2Arr);
    
    if(str1Arr.length == 0 && str2Arr.length == 0) return 65536;
    
    str1Arr.forEach(item => {
        let idx = str2Arr.indexOf(item);
        if(idx != -1){
            let hapIdx = hap.indexOf(item);
            hap.splice(hapIdx, 1);
            
            gyo.push(item);
            str2Arr.splice(idx, 1);
        }
    });
    
    return Math.floor((gyo.length / hap.length) * 65536)
}

function sliceString(str){
    let arr = [];
    
    for(let i = 0; i < str.length - 1; i++){
        let sliceStr = str[i] + str[i+1];
        if(sliceStr.search(/[^a-zA-Z]/g) == -1) arr.push(sliceStr.toUpperCase());
    }
    
    return arr;
}