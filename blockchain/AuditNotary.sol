// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AuditNotary {
    // This list will store all our attack hashes (The CID Hashes)
    string[] public attackHashes;

    // This function lets us add a new hash to the blockchain
    function storeHash(string memory _hash) public {
        attackHashes.push(_hash);
    }

    // This lets us check how many logs we have saved in total
    function getAuditCount() public view returns (uint) {
        return attackHashes.length;
    }
}