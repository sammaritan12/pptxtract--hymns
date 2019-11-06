import React from "react";
import { Layout, Menu, Breadcrumb } from "antd";

import "./App.css";
import "antd/dist/antd.css";

const { Header, Content, Footer } = Layout;

function App() {
  return (
    <div className="App">
      <Header>
        <div className="logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={["2"]}
          style={{ lineHeight: "64px" }}
        >
          <Menu.Item key="1">Home</Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: "0 50px" }}>
        <Breadcrumb style={{ margin: "16px 0" }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>About</Breadcrumb.Item>
        </Breadcrumb>
        <div style={{ background: "#fff", padding: 24, minHeight: 280 }}>
          <h1>pptxtract-hymns</h1>
          <p>
            Extracts the texts from church powerpoint hymns, and places them
            into a new powerpoint.
          </p>
        </div>
      </Content>
      <Footer style={{ textAlign: "center", position: "sticky", bottom: "0" }}>
        Mark Patricio 2019.
      </Footer>
    </div>
  );
}

export default App;
