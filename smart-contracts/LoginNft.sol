// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
// import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
// import "@openzeppelin/contracts/token/ERC1155/extensions/ERC1155URIStorage.sol";
//import "@opengsn/gsn/packages/contracts/src/ERC2771Recipient.sol";
import "@openzeppelin/contracts/metatx/ERC2771Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract LoginNFT is ERC2771Context, Ownable, ERC721URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    string uri = "ipfs/QmQp2CjnHpY71s9JDVzmGUaUN8QWBuMJUHphCZaq7jmaWb";

    constructor(string memory name_, string memory symbol_,address owner,address trustedForwarder)
     ERC721(name_, symbol_) ERC2771Context(trustedForwarder) {
    }

    function mint() public  {
         _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _safeMint(_msgSender(), newItemId);
        _setTokenURI(newItemId, uri);
    }

    function _msgSender() internal view override(Context, ERC2771Context) returns(address) {
        return ERC2771Context._msgSender();
    } 

    function _msgData() internal view override(Context, ERC2771Context) returns(bytes calldata) 
    {
        return ERC2771Context._msgData();
    }  
}
