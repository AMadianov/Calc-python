Feature: Testing calc app
Feature: Testing calc app
Scenario: Testing sum
  Given website "http://127.0.0.1:5000"
  Then push button with num '1'
  Then push button with num 'plus'
  Then push button with num '2'
  Then push button with num 'equals'
  Then values element by id 'answer' = '3'
  
Scenario: Testing subtract
  Given website "http://127.0.0.1:5000"
  Then push button with num '8'
  Then push button with num 'subtract'
  Then push button with num '3'
  Then push button with num 'equals'
  Then values element by id 'answer' = '5'
  
Scenario: Testing divide
  Given website "http://127.0.0.1:5000"
  Then push button with num '2'
  Then push button with num 'divide'
  Then push button with num '2'
  Then push button with num 'equals'
  Then values element by id 'answer' = '1'
  
Scenario: Testing product
  Given website "http://127.0.0.1:5000"
  Then push button with num '3'
  Then push button with num 'product'
  Then push button with num '2'
  Then push button with num 'equals'
  Then values element by id 'answer' = '6'

Scenario: Testing clear
  Given website "http://127.0.0.1:5000"
  Then push button with num '7'
  Then push button with num 'C'
  Then values element by id 'answer' = '0'