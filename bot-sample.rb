ENV['YOUR_TOKEN'] #.env-ruby.templateに自分のtokenを書く。

require 'discordrb'

bot = Discordrb::Commands::CommandBot.new(
    token: "PUT YOUR TOKEN",
    client_id: "551639881906913310",
    prefix:'::',
)

bot.command :system do |event|  #doの前にdiscord側で打つコマンドを登録できる。
    event.send_message("hello, world.#{event.user.name},\nuser_client_number:#{event.user.id}")
end

bot.command :reaction do |event|
    event.add_reaction()
end

bot.run #起動
