Given(/^User is on contact form page$/) do
    visit "/contact/"
    expect(page).to have_content 'Contact Form'
end

When(/^User fill the fields$/) do
    fill_in 'first_name', with: 'lnwBoss'
    fill_in 'last_name', with: 'yong'
    fill_in 'email', with: 'boss@prontomarketing.com'
end

When(/^User click submit button$/) do
    click_button 'Submit'
end

Then(/^User submit form succussfully$/) do
    expect(page).not_to have_content 'This field is required'
end

Then(/^User get error message$/) do
    expect(page).to have_content 'This field is required'
end

Then(/^User should be on thank you page$/) do
    expect(page).to have_content 'Thank you!'
    expect(page).to have_content 'First name: lnwBoss'
    expect(page).to have_content 'Last name: yong'
    expect(page).to have_content 'Email: boss@prontomarketing.com'
    expect(page).to have_content 'IP:'
    expect(page).to have_content 'Lat:'
    expect(page).to have_content 'Lng:'
end
