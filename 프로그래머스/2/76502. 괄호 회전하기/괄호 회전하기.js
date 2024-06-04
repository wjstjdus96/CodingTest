function solution(s) {
    const left = ["(","[","{"];
    const right = [")","]","}"];
    let answer = 0;
    
    return s.split('').reduce((ac, v, i) => {
        let newStr = [...s.slice(i) + s.slice(0,i)];
        let stack = [newStr[0]];
        
        for(let i = 1; i < newStr.length;i++){
            let isRight = right.indexOf(newStr[i])
            if(isRight != -1){
                if(isRight == left.indexOf(stack[stack.length -1])) stack.pop();
                else stack.push(newStr[i]);
            }else{
                stack.push(newStr[i]);
            }
        }
        return stack.length == 0 ? ac+1 : ac;
    }, 0);
}
