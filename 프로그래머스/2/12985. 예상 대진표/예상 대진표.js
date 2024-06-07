function solution(n,a,b){
    for(let i = 1; Math.pow(2,i) <= n; i++){
        if(Math.max(a,b) % 2 == 0 && Math.abs(a-b) == 1){
            return i;
        }
        a = Math.round(a/2);
        b = Math.round(b/2);
    }
}