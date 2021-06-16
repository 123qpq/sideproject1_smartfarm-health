# sideproject1_smartfarm-health

#요약


  앱-서버-아두이노 형태로 연결했습니다.
  
  
  아두이노에서 데이터를 서버로 보내 저장하고 앱에서 서버의 정보를 불러옵니다.
  
  
  서버는 rest api 형태로 제작하였습니다. 서버는 NCP(NAVER CLOUD PLATFORM) 을 사용했습니다.
  
  
  첫 프로젝트라 보안과 효율성에 문제가 있을 수 있습니다.
  
  

##accounts


  계정에 관한 정보를 담고 있습니다.
  
  
  JWT를 사용하고 싶었으나 아직 제대로 활용하지 못해서 단순히 POST 방식으로 아이디와 비밀번호를 입력받습니다.
  
  
  SIGN IN 과 SIGN UP 기능이 있습니다.
