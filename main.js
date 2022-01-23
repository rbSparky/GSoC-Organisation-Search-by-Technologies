function main() {
    let input, filter, ul, li, a, i, txtValue, tags, prev = 0;
    tags = []
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();

    for (let i = 0; i < filter.length; i++) {
        if (filter[i] === ',') {
            tags.push(filter.slice(prev, i));
            prev = i + 1;
        }
    }

    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");


    for (let i = 0; i < li.length; i++) {
        

        let ptags = [],
            prev = 0;
        p = li[i].getElementsByTagName("p")[0];
        txtValue = p.textContent || p.innerText;

        for (let k = 0; k < txtValue.length; k++) {
            if (prev !== 0 && txtValue[k] === ',') {
                ptags.push(txtValue.slice(prev, k));
                prev = k + 1;
            }
            if (txtValue[k] === ':') {
                prev = k + 2;
            }
        }

        //document.getElementById("main").innerHTML = ptags;

		let get = 0;
        for (let k = 0; k < ptags.length; k++) {
            for (let j = 0; j < tags.length; j++) {
                //if (txtValue.toUpperCase().indexOf(tags[j]) > -1) {
                if (ptags[k].toUpperCase() === tags[j]) {
                    li[i].style.display = "";
                    get += 1;
                }
            }
        }
        
        if (get < tags.length) {
            li[i].style.display = "none";
        }

    }
}