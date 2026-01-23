// used to grab cities from http://www.citymayors.com/statistics/largest-cities-alphabetical.html
x = document.querySelectorAll('[bgcolor]')
arr = []
let regex = /\d/;

x.forEach((val)=>{
    if(val.tagName == "TD"){
        if (regex.test(val.innerText) === false) {
		arr.push(val.innerText)
    }    
}
})

console.log(arr)