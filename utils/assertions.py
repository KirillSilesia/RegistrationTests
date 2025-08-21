def assert_url_contains(driver, expected_path):
    current = driver.current_url
    assert expected_path in current, f"Expected '{expected_path}' in URL. Got: {current}"