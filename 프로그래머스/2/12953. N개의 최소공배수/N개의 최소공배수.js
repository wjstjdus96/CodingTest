function solution(arr) {
    let answer = arr[0];
    
    for(let i = 1; i < arr.length; i++){
        answer = (answer * arr[i]) / gcd(arr[i], answer);
    }
    return answer;
}

function gcd(a,b){
    let gcd = 1;
    
    for(let i = 1; i <= Math.min(a,b); i++){
        if(a % i == 0 && b % i == 0) gcd = i;
    }
    return gcd;
}