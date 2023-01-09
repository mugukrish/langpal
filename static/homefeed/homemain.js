const up_vote = document.querySelectorAll("#post-vote-color-up")
const down_vote = document.querySelectorAll("#post-vote-color-down")


for (let el of down_vote){

    el.addEventListener("click", () =>{
        if (el.classList.contains("bg-red-500")){
            el.classList.remove("bg-red-500")
        }
        else{
            this_ele_upvote = el.parentElement.parentElement.parentElement.getElementsByClassName("upclass")[0]

            if (this_ele_upvote.classList.contains("bg-green-500")){
                window.alert("You have already upvoted the post")
            }
            else{
                el.classList.add("bg-red-500")
            }
            
        }

    })

}


for (let el of up_vote){
    el.addEventListener("click", () =>{


        if (el.classList.contains("bg-green-500")){
            el.classList.remove("bg-green-500")
        }
        else{
            this_ele_downvote = el.parentElement.parentElement.parentElement.getElementsByClassName("downclass")[0]
            if (this_ele_downvote.classList.contains("bg-red-500")){
                window.alert("You have already downvoted the post")
            }
            else{
                el.classList.add("bg-green-500")
            }
            
        }

    })
}


// const els = document.querySelectorAll("#sy_brn");
// els.forEach(el => el.addEventListener("click", ev => alert(ev.currentTarget.classList)));