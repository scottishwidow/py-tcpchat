const net = require("net");

const server = net.createServer();

// an array of client sockets(objects)
const clients = [];

server.on("connection", (socket) => {
    console.log("A new connection received.");

    socket.on("data", (data) => {
        clients.map((s) => {
            s.write(data)
        });
    });

    clients.push(socket)
});

server.listen(3008, "127.0.0.1", () => {
    console.log("opened server on", server.address());
});
