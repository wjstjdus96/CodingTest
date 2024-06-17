function solution(n, words) {
    var saidWords = [];
    var lastWord = words[0].substr(0,1);
    
    for(let i = 0; i < words.length; i++){
        if (saidWords.includes(words[i]) || words[i].substr(0,1) != lastWord){
            let order = (i + 1) % n == 0 ? n : (i + 1) % n;
            let turn = Math.ceil((i + 1) / n );
            return [order , turn]
        }
        lastWord = words[i].slice(-1);
        saidWords.push(words[i]);
        
    }
    return[0,0]
}