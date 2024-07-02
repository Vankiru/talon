app: iterm2
-

bundle install:
  insert("bundle install")
  key(enter)

bundle spec:
  insert("bundle exec rspec ")

bundle spec clip:
  insert("bundle exec rspec ")
  edit.paste()
  key(enter)

rails console:
  insert("rails c")
  key(enter)

rails server:
  insert("rails s -b 127.0.0.1")
  key(enter)

rails (migrate | me great):
  insert("bundle exec rake db:migrate")
  key(enter)
  
redis server:
  insert("redis-server")
  key(enter)
