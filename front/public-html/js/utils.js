let url = 'http://localhost:5000/article';

fetch(url)
.then(res => res.json())
.then((out) => {
	document.getElementById("title").innerHTML = out.title;
	document.getElementById("content").innerHTML = out.content;
})
.catch(err => { throw err });