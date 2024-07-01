function solution(s){
    const str = [...s];
    let stack = [str[0]];
    let stackNum = stack.length - 1;

    for(let i = 1; i < str.length; i++){
        str[i] == stack[stackNum] ? stack.pop() : stack.push(str[i])
        stackNum = stack.length - 1
    }
    
    return stack.length == 0 ? 1 : 0
}
