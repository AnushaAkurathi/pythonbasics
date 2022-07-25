import "./App.css";
import {useState} from 'react';
 
import useFetch from "./useFetch";



function App() {
  // const [sample, setSample] = useState();
  const [isLoading, setIsLoading] = useState(false);

  const [userdata] = useFetch('http://127.0.0.1:8000/');
  
  console.log(userdata, isLoading);

  return ( 
    <div className= 'App'>
      <h2>Python Quiz Questions</h2>
  
  {/* <input type="text" value={sample} onChange = {(e) => setSample(e.target.value)}></input> */}
  {userdata.map((question) => (
    
    <div className="container"  key={question.id}><h2>Q{question.id}: {question.question}</h2>
    <ul className="questions-list">
    <li><input type="radio" name="option" value= {question.a} /> {question.a}</li><br/>
    <li><input type="radio" name="option" value= {question.b} />{question.b} </li><br/>
    <li><input type="radio" name="option" value= {question.c} />{question.c}</li><br/>
    <li><input type="radio" name="option" value= {question.d} />{question.d}</li><br/>
    <li><input type="radio" name="option" value= {question.e} />{ question.e}</li><br/>
    <button style={{backgroundColor: "yellow"}} value="submit" onClick= {(e)=> setIsLoading(true)}>Submit</button><br />

    </ul>

    {isLoading && 
    (<div>
      <p><strong>Answer is:</strong>{question.answer}</p>
      <p><strong>Explanation:</strong><br/>{question.explanation}</p>
    </div>)}
    </div>
  ))}
</div>
  );
}
 
export default App;