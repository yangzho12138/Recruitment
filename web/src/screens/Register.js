import React, { useState, useEffect } from 'react'
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link, useNavigate } from 'react-router-dom';
import { register } from '../actions/userActions';
import { useDispatch, useSelector } from 'react-redux';

export const Register = () => {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [passwordConfirm, setPasswordConfirm] = useState('')

    const navigate = useNavigate()

    const userRegister = useSelector(state => state.userRegister)
    const { error } = userRegister

    const userLogin = useSelector(state => state.userLogin)
    const { userInfo } = userLogin

    useEffect(() => {
        if(userInfo){
            navigate('/')
        }
    },[userInfo, navigate])

    const dispatch = useDispatch()
    const submitHandler = (e) => {
        e.preventDefault();

        dispatch(register(username, email, password, passwordConfirm))
    }

    return(
        <Card className='mx-3 my-3'>
            <Card.Body>
                <Form onSubmit={submitHandler}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" value={email} onChange={e => setEmail(e.target.value)}/>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="username" placeholder="Enter your name" value={username} onChange={e => setUsername(e.target.value)}/>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)}/>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <Form.Label>Confirm Password</Form.Label>
                        <Form.Control type="password" placeholder="Confirm Password" value={passwordConfirm} onChange={e => setPasswordConfirm(e.target.value)}/>
                    </Form.Group>

                    <Form.Text className="text-muted">
                        Already have an account? Click here to <Link to='/signin'>login</Link>
                    </Form.Text>
                    <br/>
                    <Form.Text className="text-muted">
                        If you have an account in the organization openDLAP, you can login in through that account directly
                    </Form.Text>
                    <br/>
                    <Button variant="primary" type='submit' className='my-3'>
                        Register
                    </Button>
                    <br/>
                    {error && (
                        <div style={{color: 'red'}}>
                            {error}
                        </div>
                    )}
                </Form>
            </Card.Body>
        </Card>
    )
}