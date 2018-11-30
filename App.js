import React, { Component } from 'react';
import logo from './dell.png';
import './App.css';
import Main from './main'


class App extends Component {
 
  state = {
    users: [],
    user : {
      u_id :[] ,
      pass: []
    }
  }
  
  componentDidMount(){
    this.getUsers();  
  }

  getUsers = _ => {
    fetch('http://localhost:4000/dashboard')
    .then(response => response.json())
    /*.then(({data}) =>
    {
      console.log(data)
    }
    )*/
    .then(response => this.setState({
      users: response.data
    }))
    .catch(err => console.error(err))
  }

  log =_ => {
      fetch(`file:///home/prithvi/Documents/DELL/index.html`)
  }; 
  addUser = _ => {

    const{user} = this.state;
    fetch(`http://localhost:4000/dashboard/add?id=${user.u_id}&password=${user.pass}`)
   //   .then(response => response.json())
      .then(this.getUsers)
      .catch(err => console.error(err))

  }

 /* validate = _ => {
    const{user} = this.state;
    fetch(`http://localhost:4000/dashboard/log?id=${user.u_id}&password=${user.pass}`)
      .then(response => response.json())
      if(response.length)
      {
        
      }
      .catch(err => console.error(err))
  }*/
  
  renderUser = ({id,password}) => 
  <div key={id}>
  {password}
  </div>
  
  render() {
    const {users,user} = this.state;
    return (
    /*  <div className="App">
        {users.map(this.renderUser)}
        <div>
          <input value={user.u_id} 
          onChange = 
          {
            e => this.setState({ user: {...user, u_id:e.target.value}})
          }
          ></input>
          <br></br>
          <br></br>
          <input type = "password" value={user.pass}
          onChange = 
          {
            e => this.setState({ user: {...user, pass:e.target.value}})
          }
          ></input>
          <br></br>
          <br></br>
          <button onClick={this.addUser}>Add User</button>
        </div>
      </div> */
      <div className="App">
          

          <div className="loginbox" >
            <img src={logo} className="avatar" alt="logo"></img>
            <h1 >DELL Product Inventory</h1>
            <form>
            <input placeholder="Username" value={user.u_id} 
          onChange = 
          {
            e => this.setState({ user: {...user, u_id:e.target.value}})
          }
          ></input>
          <br></br>
          <br></br>
          <input placeholder="Password" type = "password" value={user.pass}
          onChange = 
          {
            e => this.setState({ user: {...user, pass:e.target.value}})
          }
          ></input>
              <br></br>
              <br></br>
              <button className="loginB" onClick={this.log}>Login</button>
              
            </form>
          </div>

          <Main></Main>


      </div>
    );
  }
}

export default App;
