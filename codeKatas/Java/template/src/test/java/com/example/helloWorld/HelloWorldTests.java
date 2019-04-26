package com.example.helloWorld;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class HelloWorldTests {

	@Test
	public void test_hello() {
		HelloWorld hello = new HelloWorld();
		assertEquals("Hello", hello.sayHello());
	}
}	
