require 'faraday'
require 'json'

raise "No Slack Token Set in ENV['SLACK_TOKEN']" unless ENV['SLACK_TOKEN']
uri = "https://bendyworks.slack.com/services/hooks/incoming-webhook?token=#{ENV['SLACK_TOKEN']}"


while true do
  payload = {
    "username" => "concert_cam",
    "text" => "I'm alive as of #{Time.now.strftime("%r")}"
  }

  Faraday.post do |req|
    req.url uri
    req.headers['Content-Type'] = 'application/json'
    req.body = JSON.generate(payload)
  end

  sleep 5*60 # post every five minutes
end
