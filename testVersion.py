from version.stringVersion import versionCompare

def test_version():
    assert versionCompare('1.1', '1.2') == -1, "version2 should be greater"
    assert versionCompare('1.4', '1.2') == 1, "version1 should be greater"
    assert versionCompare('1.3', '1.3.1') == -1, "version2 should be greater"
    assert versionCompare('1.4', '1.3.12') == 1, "version1 should be greater"
    assert versionCompare('3.1.3', '3.1.3') == 0, "version1 should be equal version2"
    assert versionCompare('3.1.1', '3.1.10') == -1, "version2 should be greater"
    assert versionCompare('1.4', '1.2') == 1, "version1 should be greater"
    assert versionCompare('1.4', '1.2') == 1, "version1 should be greater"
    
    
if __name__ == "__main__":
    test_version()
    print("Everything passed")