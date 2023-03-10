import React from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useDispatch, useSelector } from 'react-redux';
import { logout } from "../actions/userActions";

export const Header = () => {

    const userLogin = useSelector(state => state.userLogin)
    const { userInfo } = userLogin

    const dispatch = useDispatch()
    const logoutHandler = () => {        
        dispatch(logout())
    }

    return(
        <header>
            <Navbar bg="dark" variant="dark">
                <Container>
                <Navbar.Brand href="/">
                    <img
                    alt=""
                    src="https://th.bing.com/th/id/OIP.aeHoebZ2cILe37CThBPCMwAAAA?w=146&h=150&c=7&r=0&o=5&dpr=2&pid=1.7"
                    width="30"
                    height="30"
                    className="d-inline-block align-top mx-3"
                    />
                    Opportunity At UIUC
                </Navbar.Brand>
                {userInfo ? (
                    <Nav className="me-end">
                        <Nav.Link href="/resume">Welcome {userInfo.username}</Nav.Link>
                        <Nav.Link onClick={logoutHandler}>Signout</Nav.Link>
                    </Nav>
                ) : (
                    <Nav className="me-end">
                        <Nav.Link href="/signin">Student</Nav.Link>
                        <Nav.Link href="http://127.0.0.1:8000/admin">Admin</Nav.Link>
                    </Nav>
                )}
                </Container>
            </Navbar>
        </header>
        )
}