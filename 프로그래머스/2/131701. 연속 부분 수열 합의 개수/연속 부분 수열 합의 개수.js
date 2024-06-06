function solution(elements) {
    const li = [...elements, ...elements]
    const answer = []
    
    for(let i=1; i < elements.length; i++){
        for(let j = 0; j < li.length - i; j++){
            const val = li.slice(j, j+i).reduce((acc,cur) => acc + cur, 0)
            answer.push(val)
        }
    }
    
    return [...new Set(answer)].length + 1
}