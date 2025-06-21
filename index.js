$("#jokebtn").click(
    function(){
        $.ajax({
            url:"https://official-joke-api.appspot.com/random_joke",
            method:'GET',
            success:function(response){
                console.log
                $('#joketxt').text(response.setup+"--->"+response.punchline);
            },
            error:function(){
                $("#joketxt").text("Not able to connect check your Internet Connection")
            }
        })
    }
)





























/*console.log("Hello World");
var n=1;
n=null;
console.log(typeof(n));

let student={
    name:"vasu",
    age:20,
    mobile:9347021778,
    reg:1461

}
student.name="sudha"

console.log(student.name);
console.log(student['name']);

let color=['blue','violet','pink','orange','green']
color[5]="black"
console.log(color.indexOf("blue"))
console.log(color.length)
for( i=0;i<color.length;i++)
{
    console.log(color[i])
}
function myFunction(num1,num2)
{
    return num1+num2
}
console.log(myFunction(54,46))

class Student{
    constructor()
    {
        this.age=18
        this.name="vasu"
    }
    getName(){
        return this.name
    }
    setName(str)
    {
        this.name=str
    }
}
let sobj=new Student()
console.log(sobj.getName())

*/


